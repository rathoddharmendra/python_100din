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
  


  const scrollDown = document.querySelector('.scroll-down');
  scrollDown.addEventListener('click', () => {
    const target = document.querySelector('.upcoming-events');
    target.scrollIntoView({ behavior: 'smooth' });
  }
  );
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


  // city selector
  document.getElementById('city-selector').addEventListener('click', toggleDropdown);
  function toggleDropdown() {
    const dropdown = document.getElementById('city-dropdown');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    document.getElementById('city-search').focus();
  }

  function selectCity(city) {
    document.getElementById('selected-city').textContent = city;
    document.getElementById('city-dropdown').style.display = 'none';
    // Optional: trigger event reload by city
  }

  function filterCities() {
    const input = document.getElementById('city-search').value.toLowerCase();
    const items = document.querySelectorAll('#city-list li');
    items.forEach(li => {
      const match = li.textContent.toLowerCase().includes(input);
      li.style.display = match ? 'block' : 'none';
    });
  }

  // Optional: Close dropdown when clicking outside
  window.addEventListener('click', (e) => {
    if (!e.target.closest('.city-selector')) {
      document.getElementById('city-dropdown').style.display = 'none';
    }
  });



  // Event listener for the "See More" button
  // create event page
  // const slides = document.querySelectorAll('.event-form-carousel-slide');
  // let current = 0;

  // setInterval(() => {
  //   slides[current].classList.remove('active');
  //   current = (current + 1) % slides.length;
  //   slides[current].classList.add('active');
  // }, 1000);