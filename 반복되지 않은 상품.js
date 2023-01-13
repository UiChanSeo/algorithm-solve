//예) ["Apple", "Computer", "Apple", "Bag"]  => "Computer"
//
//--> Example Code : 
function firstUniqueProduct(products) {
  let map = new Map();
  products.forEach(p => {
    if(map.has(p)) {
      map.set(p, map.get(p) + 1);
    } else {
      map.set(p, 1);
    }
  });
  let name = null;
  map.forEach((v,k) => {
    if (v == 1) {
      if(!name) name = k;
    }
  });
  return name;
}
console.log(firstUniqueProduct([ "Apple", "Computer", "Apple", "Bag" ]));
