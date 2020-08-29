class Binary {
  constructor(array) {
    this.list = array;
    this.list.sort(function (a, b) {
      return b - a;
    });
    this.list.reverse();
    console.log("Sorted list: " + this.list);
    this.length = this.list.length;
  }

  search(target) {
    let left = 0;
    let right = this.length - 1;
    //let middle;

    while (left <= right) {
      let middle = Math.floor((left + right) / 2);
      if (this.list[middle] < target) {
        left = middle + 1;
      } else if (this.list[middle] > target) {
        right = middle - 1;
      } else {
        return middle;
      }
    }
    return target + " Doesn't exist in the given list";
  }
}

module.exports = Binary;
