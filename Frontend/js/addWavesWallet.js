// Функция, которая создаёт новый адрес
function createAdress() {
    const Waves = WavesAPI.create(WavesAPI.TESTNET_CONFIG);                // Врубаем апишку
    var youSeed = $('input[name="youSeed"]').val().toString();             // Наш seed
    console.log(youSeed);
    const anotherSeed = Waves.Seed.fromExistingPhrase(youSeed);            // Шифруем seef
    var youAdress = $('input[name="youAdress"]').val(anotherSeed.address); // Выводим адрес на экран  
}

function Encription() {
    var serverString = $('input[name="serverString"]').val(); // Строка, которую надо скрестить с публичным адресом и зашифровать
    var privateKey = $('input[name="privateKey"]').val();     // Строка с приватным ключом
    
    var ciphertext = CryptoJS.AES.encrypt(JSON.stringify(privateKey), serverString); // Шифруем ключ + private key
    
    $('input[name=endKey]').val(ciphertext.toString());                     // Показываем шифрокод в 3-й строчке              
    
    // var takeCipher = $('input[name=endKey]').val();                         // Получаем значение шифрокода

    // var bytes  = CryptoJS.AES.decrypt(takeCipher.toString(), serverString); // Дешифруем   
    // var decryptedData = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));      // В норм формат переводим

    // console.log(decryptedData);
    }

// RSA signature generation
// var sig = new KJUR.crypto.Signature({"alg": "SHA384withECDSA"});
// sig.init(sCertPEM);
// sig.updateString('aaa');
// var hSigVal = sig.sign();

// var crypto = require('crypto') //Node.js or Browserify (browser)

// var ecdsa = require('ecdsa')
// var sr = require('secure-random') //npm install --save secure-random@1.x
// var ck = new CoinKey(privateKey, true) // true => compressed public key / addresses

// var msg = new Buffer("hello world!", 'utf8')
// var shaMsg = crypto.createHash('sha256').update(msg).digest()
// var signature = ecdsa.sign(shaMsg, ck.privateKey)
// var isValid = ecdsa.verify(shaMsg, signature, ck.publicKey)
// console.log(isValid) //true

