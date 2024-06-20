#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let height = 0; height < this.height; height++) {
      let rectangle = '';
      for (let width = 0; width < this.width; width++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
}
module.exports = Rectangle;
