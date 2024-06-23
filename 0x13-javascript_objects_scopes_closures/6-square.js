#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let height = 0; height < this.height; height++) {
        let rectangle = '';
        for (let width = 0; width < this.width; width++) {
          rectangle += c;
        }
        console.log(rectangle);
      }
    }
  }
};
