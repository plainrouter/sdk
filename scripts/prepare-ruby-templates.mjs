import { execFileSync } from 'node:child_process';
import { writeFile } from 'node:fs/promises';
import { join } from 'node:path';

const [generatorJar, output] = process.argv.slice(2);
if (!generatorJar || !output) {
  throw new Error('usage: prepare-ruby-templates.mjs GENERATOR_JAR OUTPUT_DIRECTORY');
}

let template = execFileSync('unzip', ['-p', generatorJar, 'ruby-client/api.mustache'], {
  encoding: 'utf8',
});
let apiClientTemplate = execFileSync('unzip', ['-p', generatorJar, 'ruby-client/api_client.mustache'], {
  encoding: 'utf8',
});
const parameter = "{{#required}}{{{paramName}}}{{/required}}{{^required}}opts[:'{{{paramName}}}']{{/required}}";
// Leave string values unchanged on the wire; the server validates their bounds.
const numericOnly = `{{#isInteger}}!${parameter}.is_a?(String) && {{/isInteger}}`
  + `{{^isInteger}}{{#isLong}}!${parameter}.is_a?(String) && {{/isLong}}{{/isInteger}}`;

for (const [operator, bound] of [['>', 'Maximum'], ['<', 'Minimum']]) {
  const comparison = `${parameter} ${operator}{{#exclusive${bound}}}`;
  if (template.split(comparison).length !== 2) {
    throw new Error(`Expected one Ruby ${bound.toLowerCase()} comparison in the pinned template.`);
  }
  template = template.replace(comparison, numericOnly + comparison);
}

const marcelRequire = "require 'marcel'";
if (apiClientTemplate.split(marcelRequire).length !== 2) {
  throw new Error('Expected one Marcel require in the pinned Ruby API client template.');
}
apiClientTemplate = apiClientTemplate.replace(marcelRequire, `${marcelRequire}\nrequire 'pathname'`);

await writeFile(join(output, 'api.mustache'), template);
await writeFile(join(output, 'api_client.mustache'), apiClientTemplate);
