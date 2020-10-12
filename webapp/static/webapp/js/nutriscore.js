var nutriscore = document.querySelector(".nutriscore_char").textContent;
var char_class = "nutriscore_char_";
var ring_class = "nutriscore_ring_"

function nutriscore_color(nutriscore, letter, ring){
    nutriscore = nutriscore.replace(/\s/g, '');
    document.querySelector(".nutriscore_char").classList.add(letter + nutriscore);
    document.querySelector(".nutriscore_ring ").classList.add(ring + nutriscore);
}

// window.onload = function() {
//     nutriscore_color(nutriscore, letter_class, ring_class);

var nutri_block = document.getElementsByClassName("nutriscore_img");
window.onload = function() {
    for(var i = 0; i < nutri_block.length; i++)
    {
        nutriscore_color(nutriscore[i], char_class, ring_class);
    }
};