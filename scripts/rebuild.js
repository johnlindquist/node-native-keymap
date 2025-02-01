#!/usr/bin/env node

const { spawnSync } = require('child_process');
const path = require('path');

// Set environment variables to force C++20
process.env.CXXFLAGS = process.env.CXXFLAGS ? `${process.env.CXXFLAGS} -std=c++20` : '-std=c++20';
process.env.CFLAGS = process.env.CFLAGS ? `${process.env.CFLAGS} -std=c++20` : '-std=c++20';

// Run electron-rebuild
const result = spawnSync('pnpm', [
  'exec',
  'electron-rebuild',
  '-f',
  '-w',
  '@johnlindquist/native-keymap',
  '-v',
  '32.0.0' // Electron 32 version
], {
  stdio: 'inherit',
  shell: true
});

if (result.status !== 0) {
  console.error('Failed to rebuild native module');
  process.exit(1);
}