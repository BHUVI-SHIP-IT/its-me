/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    let resultsArr = [];
    let completedFn = 0;

    return new Promise(function(resolve, reject) {
        functions.forEach((fn, index) => 
        fn().then(
            result => {
                resultsArr[index] = result;
                completedFn += 1
                if (completedFn == functions.length) {
                    resolve(resultsArr)
                }
            },
            error => reject(error)
        ))
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */