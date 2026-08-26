import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { readdir } from 'node:fs/promises';
import test from 'node:test';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);
const site = new URL('..', import.meta.url);

async function filesBelow(directory, prefix = '') {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
    if (entry.isDirectory()) files.push(...await filesBelow(new URL(`${entry.name}/`, directory), relative));
    else files.push(relative);
  }
  return files.sort();
}

test('packages exactly the allowlisted public Pages assets', async () => {
  await execFileAsync('sh', ['build-static-assets.sh'], { cwd: site });

  const sourceAssets = await filesBelow(new URL('assets/', site));
  const outputFiles = await filesBelow(new URL('dist/', site));
  const expected = [
    'index.html',
    'script.js',
    'styles.css',
    ...sourceAssets.map((file) => `assets/${file}`),
  ].sort();
  assert.deepEqual(outputFiles, expected);
  assert.deepEqual((await readdir(new URL('dist/', site))).sort(), ['assets', 'index.html', 'script.js', 'styles.css']);
  for (const forbidden of [
    'PHASE-B-SETUP.md', 'migrations', 'tests', 'package.json', 'functions', '.gitignore',
    'build-static-assets.sh',
  ]) {
    assert.ok(!outputFiles.some((file) => file === forbidden || file.startsWith(`${forbidden}/`)));
  }
});
