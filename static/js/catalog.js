document.addEventListener("DOMContentLoaded", function () {


    const search = document.getElementById("bookSearch");

    const books = document.querySelectorAll("[data-book]");


    search.addEventListener("keyup", function () {


        let value = search.value.toLowerCase();



        books.forEach(function(book){


            let text = book.innerText.toLowerCase();



            if(text.includes(value)){


                book.style.display = "block";


            } else {


                book.style.display = "none";


            }


        });



    });



});