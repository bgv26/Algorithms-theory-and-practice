process.stdin.setEncoding('utf8');

const modulo = (n, m) => {
    if (n.length < 16) {
        return n % m;
    }

    let rest = '';
    let divident = '';

    for (let i = 0; i < n.length; i++) {
        divident += rest + n[i];
        rest = '';
        if (parseInt(divident) >= m) {
            rest = divident % m;
            divident = '';
        }
    }

    return rest + '' + divident;
};

let n = 0;
let m = 0;

process.stdin.on('readable', () => {
    let chunk = process.stdin.read();
    if (chunk !== null) {
        let arr = chunk.split(' ');
        n = arr[0];
        m = parseInt(arr[1]);
    }
});

process.stdin.on('end', () => {
    let fibNumbers = [0, 1];
    let periodLength = 0;

    for (let i = 2; i < 6 * m; i++) {
        fibNumbers[i] = (fibNumbers[i - 1] + fibNumbers[i - 2]) % m;
        if (fibNumbers[i - 1] === 0 && fibNumbers[i] === 1) {
            periodLength = i - 1;
            break;
        }
    }

    process.stdout.write(fibNumbers[modulo(n, periodLength)].toString());
});