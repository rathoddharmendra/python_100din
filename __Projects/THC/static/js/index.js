// let isNavOpen = false;

//     function toggleNav(){
//         if (!isNavOpen){
//             openNav()
//         } 
//         else {
//             closeNav()
//         }
//         isNavOpen = !isNavOpen;
//     }
//     function openNav() {
//         document.getElementById("mySidebar").style.width = "250px";
//         document.getElementById("main").style.marginLeft = "250px";
//     }

//     function closeNav() {
//         document.getElementById("mySidebar").style.width = "0";
//         document.getElementById("main").style.marginLeft= "0";
//     }


// // Example starter JavaScript for disabling form submissions if there are invalid fields
// (() => {
//     'use strict'
  
//     // Fetch all the forms we want to apply custom Bootstrap validation styles to
//     const forms = document.querySelectorAll('.needs-validation')
  
//     // Loop over them and prevent submission
//     Array.from(forms).forEach(form => {
//       form.addEventListener('submit', event => {
//         if (!form.checkValidity()) {
//           event.preventDefault()
//           event.stopPropagation()
//         }
  
//         form.classList.add('was-validated')
//       }, false)
//     })
//   })()
  

  const images = document.querySelectorAll('.carousel-img');
  let index = 0;

  setInterval(() => {
    // Remove current classes
    images[index].classList.remove('active');
    images[(index + 1) % 3].classList.remove('top');
    images[(index + 2) % 3].classList.remove('bottom');

    // Move index forward
    index = (index + 1) % 3;

    // Apply new roles
    images[index].classList.add('active');
    images[(index + 1) % 3].classList.add('top');
    images[(index + 2) % 3].classList.add('bottom');
  }, 2000); // 2 seconds delay between rotations
