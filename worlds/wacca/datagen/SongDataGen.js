import waccaSongs from "./waccaSongsPlus.js";
//Data taken from https://github.com/Stabyourself/mithical/blob/master/assets/wacca/waccaSongsPlus.js

import * as fsp from 'fs/promises';

await fsp.writeFile('./waccaSongData.json', JSON.stringify(waccaSongs));