/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    var answer=[];
    var cur=[];

    for(var i=0;i<arr.length;++i){
        cur.push(arr[i]);
        if(cur.length==size){
            answer.push(cur);
            cur=[];
        }
    }
    if(cur.length!=0) answer.push(cur);
    return answer;
};
