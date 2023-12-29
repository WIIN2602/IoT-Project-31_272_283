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