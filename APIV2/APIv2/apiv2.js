// get the id dataOutput from the index,html file and pass it to the dataOutut variable
const dataOuput = document.querySelector("#dataOutput")

// create an asynchronous function to fetch the data
async function getData(){
    // function body (Write code heree)
    // wait for resonse from the API you fetchng data from
    const response = await fetch("https://hp-api.onrender.com/api/characters")

    // wait for response and convert to JSOn upon receipt
    const apiData = await response.json()

    return (apiData)
}

// /add event listed to wait for for page to load before fetching the API DATA
document.addEventListener("DOMContentLoaded", async ()=>{
// create an array to stire data fectched from the API
let apiData = []

// Use try and catch to deal with errors when fetching data/APi data
try {
    // try and call th function and if successful, store it into the array apiData on line 19
    apiData = await getData()
} // if unsuccessful, log the erro in the console
catch (error){
    console.log(error)
}

//loop through the data received from the API

for (let {name, image,} of apiData ){

    //create a div element
    const cardContainer = document.createElement('div')
    // add the style "cardContainer"  from the style.css file to the div above
    cardContainer.classList.add('cardContainer')

     //create a div element
    const imageContainer = document.createElement('div')
    // add the style "imageContainer"  from the style.css file to the div above
    imageContainer.classList.add('imageContainer')

     //create an h2 element
    const characterName =document.createElement('h2')
     //get the value associated with the name property from the
     // object and insert it to the h2 element created above
    characterName.innerText = `${name}`


     // add the the name of the character to the card container
     cardContainer.append(characterName)

     
     // add the the image of the character to the card container
     cardContainer.append(imageContainer)

    //create an an  image element to display the image <img src="./myPic.png" alt="">
    const characterImage = document.createElement('img')

    // Add a src attribute to the image element created above
    characterImage.setAttribute('src', image)

    // add  the image to the image container
    imageContainer.append(characterImage)

    // add the cardcontainer div to the document inside the div with the id = dataOutput
    dataOuput.append(cardContainer)
}
})





// https://www.w3schools.com/jsref/met_element_setattribute.asp
// The setAttribute() method sets a new value to an attribute.

// If the attribute does not exist, it is created first.