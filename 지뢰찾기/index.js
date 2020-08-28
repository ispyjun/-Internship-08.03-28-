
var dataset = [];
var tbody = document.querySelector('#table tbody');
var stop=false;
var open=0;
let clearCell = 0;
document.querySelector('#exec').addEventListener('click', function () {
    tbody = document.querySelector('#table tbody');
    tbody.innerHTML = '';
    document.querySelector('#result').textContent='';
    dataset = [];
    stop=false;
    open=0;
    clearCell = 0;
    var hor = parseInt(document.querySelector('#hor').value);
    var ver = parseInt(document.querySelector('#ver').value);
    var mine = parseInt(document.querySelector('#mine').value);
    //console.log(hor, ver, mine);

    //지뢰 위치 뽑기
    var candidate = Array(hor * ver)
        .fill()
        .map(function (element, index) {
            return index;
        });
    var shuf = [];

    while (candidate.length > hor* ver-mine) {
        var moving = candidate.splice(Math.floor(Math.random() * candidate.length), 1)[0];
        shuf.push(moving);
    }
    //console.log(shuf);

    //지뢰 테이블 만들기
    var dataset = [];
    var tbody = document.querySelector('#table tbody');
    for (var i = 0; i < ver; i += 1) {
        var arr = [];
        var tr = document.createElement('tr');
        dataset.push(arr);
        for (var j = 0; j < hor; j += 1) {
            arr.push(1);
            var td = document.createElement('td');
            td.addEventListener('contextmenu', function (e) {
                e.preventDefault();
                var partr = e.currentTarget.parentNode;
                var partbody = e.currentTarget.parentNode.parentNode;
                var kan = Array.prototype.indexOf.call(partr.children, e.currentTarget);
                var jul = Array.prototype.indexOf.call(partbody.children, partr);
                
                console.log(partr, partbody, e.currentTarget, kan, jul);
                if (e.currentTarget.textContent === '' || e.currentTarget.textContent === 'X') {
                    e.currentTarget.textContent = '🚩';
                } else if (e.currentTarget.textContent === '🚩') {
                    e.currentTarget.textContent = '?';
                } else if (e.currentTarget.textContent === '?') {
                    if (dataset[jul][kan] === 1) {
                        e.currentTarget.textContent = '';
                    } else if (dataset[jul][kan] === 'X') {
                        e.currentTarget.textContent = '';
                    }
                }
            });
            td.addEventListener('click', function (e) {
                if(stop){
                    return;
                }

                var partr = e.currentTarget.parentNode;
                var partbody = e.currentTarget.parentNode.parentNode;
                var kan = Array.prototype.indexOf.call(partr.children, e.currentTarget);
                var jul = Array.prototype.indexOf.call(partbody.children, partr);
                
                if(dataset[jul][kan]===0){
                    return;
                }
                e.currentTarget.classList.add('opened');
                open+=1;
                
                if (dataset[jul][kan] === 'X') {
                    e.currentTarget.textContent = '💥';
                    document.querySelector('#result').textContent='실패';
                    stop=true;
                } else {
                    var near = [
                        dataset[jul][kan - 1], dataset[jul][kan + 1]
                    ];
                    if (dataset[jul - 1]) {
                        near = near.concat([dataset[jul - 1][kan - 1], dataset[jul - 1][kan], dataset[jul - 1][kan + 1]]);
                    }
                    if (dataset[jul + 1]) {
                        near = near.concat([dataset[jul + 1][kan - 1], dataset[jul + 1][kan], dataset[jul + 1][kan + 1]]);
                    }
                    let nearMine = near.filter(function (v) {
                        return v === 'X';
                    }).length;
                    e.currentTarget.textContent = nearMine || '';
                    dataset[jul][kan]=1;
                    if (nearMine === 0) {
                        var nearKan = [];
                        if (tbody.children[jul - 1]) {
                            nearKan = nearKan.concat([
                                tbody.children[jul - 1].children[kan - 1],
                                tbody.children[jul - 1].children[kan],
                                tbody.children[jul - 1].children[kan + 1]
                            ]);
                        }
                        nearKan = nearKan.concat([
                            tbody.children[jul].children[kan - 1],
                            tbody.children[jul].children[kan + 1]
                        ]);
                        if (tbody.children[jul + 1]) {
                            nearKan = nearKan.concat([
                                tbody.children[jul + 1].children[kan - 1],
                                tbody.children[jul + 1].children[kan],
                                tbody.children[jul + 1].children[kan + 1]
                            ]);
                        }
                        /*nearKan.filter(function(v){
                            return !!v;
                        }).forEach(function(nextKan){
                            var partr=nextKan.parentNode;
                            var partbody=nextKan.parentNode.parentNode;
                            var nextKanKan=Array.prototype.indexOf.call(partr.chiledren,nextKan);
                            var nextKanJul=Array.prototype.indexOf.call(partbody.chiledren,partr);
                            if(dataset[nextKanJul][nextKanKan]!=1){
                                nextKan.click();
                            }
                        });*/
                        nearKan.filter(function (v) { return !!v; }).forEach(function (nextkan) {
                            nextkan.click();
                        });
                    }
                }
                console.log(open,hor*ver-mine);
                if(open===hor*ver-mine){
                    stop=true;
                    document.querySelector('#result').textContent='승리';
                }
            });
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
   // console.log(dataset);
    //console.log(shuf.length);

    //지뢰 심기
    for (var k = 0; k < shuf.length; k++) {
        vert = Math.floor(shuf[k] / 10);
        hori = shuf[k] % 10;
        //console.log(vert, hori);
        tbody.children[vert].children[hori].textContent = '';
        dataset[vert][hori] = 'X';
    }
});
