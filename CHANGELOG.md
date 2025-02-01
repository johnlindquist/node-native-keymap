# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [3.3.9](https://github.com/johnlindquist/node-native-keymap/compare/v3.3.8...v3.3.9) (2025-02-01)

### [3.3.8](https://github.com/johnlindquist/node-native-keymap/compare/v3.3.7...v3.3.8) (2025-02-01)


### Bug Fixes

* add pkg-config and apt update to CI workflow ([746f7d9](https://github.com/johnlindquist/node-native-keymap/commit/746f7d91ea63f7379a2595496aa3941c41eed033))
* add X11 dependencies to publish job ([9e0f925](https://github.com/johnlindquist/node-native-keymap/commit/9e0f925c9cc9e4fcdec57946b23fd3514de726a9))
* **ai:** let composer attempt to support Electron 32 ([5f5e870](https://github.com/johnlindquist/node-native-keymap/commit/5f5e8707300572f87d7bbc6fe78d383b21c1ec50))
* **build:** test ([b4629f2](https://github.com/johnlindquist/node-native-keymap/commit/b4629f21695500da9752b3f290a71120c7e21873))
* **build:** test ([9f31481](https://github.com/johnlindquist/node-native-keymap/commit/9f31481ad2780e94572a81ce16c1a4ccb2e4c616))
* **build:** test ([53ecca3](https://github.com/johnlindquist/node-native-keymap/commit/53ecca3f9c93be95f9d2e4704732c72d4385e8f3))
* **build:** test ([db41e51](https://github.com/johnlindquist/node-native-keymap/commit/db41e51f70cff6b94032c98684231d48dd8f5f33))
* **build:** test ([39fe264](https://github.com/johnlindquist/node-native-keymap/commit/39fe26421bc52cbc1d59d015a3606309ffe5e009))
* **build:** test ([333b1f3](https://github.com/johnlindquist/node-native-keymap/commit/333b1f3b48b15afaeaa4ba121dcab681b268e58e))
* **build:** test ([299c3d5](https://github.com/johnlindquist/node-native-keymap/commit/299c3d5d06927f8899ba8685ea67e08d7dd133bd))
* **build:** test ([3533a08](https://github.com/johnlindquist/node-native-keymap/commit/3533a083b42f3c498f61bdf22dbf38423643b77c))
* **build:** test ([c78dcae](https://github.com/johnlindquist/node-native-keymap/commit/c78dcae724f71c74a32ee6229437a0e7e54d8578))
* **build:** test ([b44ca16](https://github.com/johnlindquist/node-native-keymap/commit/b44ca162c9b7d1b7ca4856751d0ad4758708b486))
* **build:** test ([419a00c](https://github.com/johnlindquist/node-native-keymap/commit/419a00c39cfe6ccb719acf0e84c89e8b54e0fc28))
* **build:** test ([f2f9bce](https://github.com/johnlindquist/node-native-keymap/commit/f2f9bceec88c14353ebe0f10a75d004621d74a8b))
* **build:** test ([dc3bcae](https://github.com/johnlindquist/node-native-keymap/commit/dc3bcae06235b06f3cebeea8bfe794825e022d18))
* **build:** test ([ea201ad](https://github.com/johnlindquist/node-native-keymap/commit/ea201ad52da54151d6f108bc17f213bc0bba9804))
* **ci:** copy binding.gyp to test project ([12dd7be](https://github.com/johnlindquist/node-native-keymap/commit/12dd7befd5bb10e3a71430baeef9911d1ab6ba77))
* **ci:** copy deps directory to test project ([2445260](https://github.com/johnlindquist/node-native-keymap/commit/2445260dc86e9ef7d49e45676369f2768efdfbbd))
* **ci:** copy src directory to test project ([64944d7](https://github.com/johnlindquist/node-native-keymap/commit/64944d7bf451476a9849f574a451f408f125dd05))
* **ci:** install node-gyp globally ([a3cd113](https://github.com/johnlindquist/node-native-keymap/commit/a3cd11386a0d167e9237920e37a1b250d7579a04))
* **ci:** install X11 development libraries ([4f63d90](https://github.com/johnlindquist/node-native-keymap/commit/4f63d903aee7e58cbad09b26eaeb851af67cd265))
* **ci:** revert to original build script ([67c088a](https://github.com/johnlindquist/node-native-keymap/commit/67c088a3eec3637e0449eaea22c34b273a325e2f))
* **ci:** switch to pnpm for CI/CD ([6dc4e71](https://github.com/johnlindquist/node-native-keymap/commit/6dc4e7151733906f23413a71853d8ad92bb66ce6))
* **ci:** use electron 32 and add retries ([4744021](https://github.com/johnlindquist/node-native-keymap/commit/474402118b449063e3b58e96f55146da940feb88))
* **ci:** use stable electron version and add retries ([00f5680](https://github.com/johnlindquist/node-native-keymap/commit/00f56801a7c1d7ed2c4646e91541e02e5b12d3f2))
* **deps:** adding node-gyp ([86813f3](https://github.com/johnlindquist/node-native-keymap/commit/86813f3e34308c5f7e3887823268f2a953072bc3))

### 3.3.7 (2024-08-22)


### Bug Fixes

* actually open and close the handle scope ([13796d8](https://github.com/johnlindquist/node-native-keymap/commit/13796d8ea1a5ef9389899f583e0b2996e8334b0c))
* add an napi handle scope for the callback ([dd9c66e](https://github.com/johnlindquist/node-native-keymap/commit/dd9c66e5a2f462ce5e366ab06c592ca40a50e01e))
* add clean up hook to remove listener on env destroy ([2d91541](https://github.com/johnlindquist/node-native-keymap/commit/2d9154159ef2fa75f73da4c5b0b3027aaccdf6d5))
* missing handlescope on windows ([2c0e6eb](https://github.com/johnlindquist/node-native-keymap/commit/2c0e6eb65c16711ba673bdd9d0f2c9e023390e4b))
* opt-out for nogc finalizer change ([#59](https://github.com/johnlindquist/node-native-keymap/issues/59)) ([d0f4fb5](https://github.com/johnlindquist/node-native-keymap/commit/d0f4fb507bf5e3551775338db4732038060d5aef))
* **publish:** attempting to build ([dba75b6](https://github.com/johnlindquist/node-native-keymap/commit/dba75b6d575dba935c19ee36c0338638ca9e5175))
* **publish:** attempting to build ([0bcd9ca](https://github.com/johnlindquist/node-native-keymap/commit/0bcd9ca620fdfe8af0f3132a3cc66a4698332cb5))
* **publish:** attempting to build ([4549dde](https://github.com/johnlindquist/node-native-keymap/commit/4549ddedd11f2e656c913bba9c3b41dcdfcf2b0f))
* **publish:** attempting to build ([fae0a4c](https://github.com/johnlindquist/node-native-keymap/commit/fae0a4cef848369edf8c6857488a2d3734bade03))
* Use SpectreMitigation attribute ([#50](https://github.com/johnlindquist/node-native-keymap/issues/50)) ([4cae698](https://github.com/johnlindquist/node-native-keymap/commit/4cae698237ba2fa3b8a0190d980d0f772534ca79))
