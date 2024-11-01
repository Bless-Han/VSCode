function getWord() {
    fetch("https://random-word-api.herokuapp.com/word")
    .then(res=>res.json())
    .then(word=>document.getElementById("random_word").innerText=word[0])
    .catch(err=>console.log(err));
}

getWord();
console.log('hello world!!')