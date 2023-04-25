// console.log("hello, I am working! ")

let profileImg = document.getElementById('p-img');

// profileImg.addEventListener('click', function(){
//     console.log("Clicked")
//     let elem = document.getElementById('p-items');
//     if (elem.style.display = "none"){
//         elem.style.display = "inline-block";

//     }
//     else if(elem.style.display = "inline-block"){

//         elem.style.display = "none"
//     }
    


// })

let active = true;
let elem = document.getElementById('p-items');

const profileSlider = function(){

    console.log("Working ! ");
    

    if (active){
        elem.style.display = "flex";
        active = false;

    }
    else {

        elem.style.display = "none"
        active = true;
    }
    
}

document.getElementById('my-container').onclick = function(e) {
    if(e.target != document.getElementById('p-items')) {
        
        elem.style.display = "none"
    } 
  }