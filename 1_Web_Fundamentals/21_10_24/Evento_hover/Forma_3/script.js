document.addEventListener("DOMContentLoaded", function () {




let block = document.getElementById("block");

block.addEventListener("mouseover", function(){
    block.style.backgroundColor = "lime";
});

block.addEventListener("mouseout", function(){
    block.style.backgroundColor = "silver";
}
);

});