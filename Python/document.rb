console.log(document)

document.getElementsById('title')
document.getElementsById('title').id
document.getElementsById('title').class
output-undefined
document.getElementsById('title').className
output-'heading'
document.getElementsById('title')getAttribute('id')
output-'title'
document.getElementsById('title')getAttribute('class')
output-'heading'
document.getElementsById('title')getAttribute('class','heads')
output-undefined
title .style.backgroundColor="red"
title .style.borderRadius="20px"
document.querySelector("h1")//h1 ke andar jo bhi kiya hai wo sab show hoga
document.querySelector("#title")//title ke ander jo bhi likha hai wo sab show hoga