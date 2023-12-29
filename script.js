function LearnMoreBTN() {
    window.location.href="learnmore.html"
}

document.addEventListener("DOMContentLoaded", function () {
    // เลือก form ด้วย ID
    const signupForm = document.getElementById("signupForm");

    signupForm.addEventListener("submit", function (event) {
      // ป้องกันการส่ง form ไปยัง URL ที่ระบุใน attribute action
      event.preventDefault();

      // ตรวจสอบว่าข้อมูลทั้งหมดถูกกรอกหรือไม่
      if (validateForm()) {
        // ถ้าข้อมูลถูกต้อง นำทางไปยังหน้า index.html
        window.location.href = "index.html";
      } else {
        // หากข้อมูลไม่ถูกต้อง สามารถจัดการเพิ่มเติมได้ตามต้องการ
        alert("กรุณากรอกข้อมูลให้ครบทุกช่อง");
      }
    });

    // ฟังก์ชันสำหรับตรวจสอบว่าข้อมูลถูกกรอกครบทุกช่องหรือไม่
    function validateForm() {
      const inputs = document.querySelectorAll(".inputs");
      for (const input of inputs) {
        if (input.value.trim() === "") {
          return false;
        }
      }
      return true;
    }
  });

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

function dropdownFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
