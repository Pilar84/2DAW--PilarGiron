function ordenarArray(array) {
    //devolver un array de menor a mayor sin usar sort()
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = 0; j < array.length - 1 - i; j++) {
            if (array[j] > array[j+1]) {
                //intercambiar valores
                let temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }   
        }
    }
    return array;
}   

//ejemplo de uso
let arr = [10, 8, 1, 3, 5];
console.log(ordenarArray(arr));  
