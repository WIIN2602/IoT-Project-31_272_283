$(document).ready(function() {
    $('#submitBtn').click(function(event) {
      event.preventDefault(); // ป้องกันการโหลดหน้าเว็บใหม่เมื่อคลิก Submit
  
      // ตรวจสอบเงื่อนไขที่ต้องการ
      var roomAvailability = true; // สมมติว่ามีห้องว่าง
  
      if (roomAvailability) {
        // หากมีห้องว่าง
        $('#roomAvailability').html('<p>จองห้องเสร็จสิ้น</p>'); // เปลี่ยนเนื้อหาของ div ที่มี id="roomAvailability" เพื่อแสดงผล
      } else {
        // หากไม่มีห้องว่าง
        $('#roomAvailability').html('<p>จองห้องล้มเหลว</p>'); // เปลี่ยนเนื้อหาของ div ที่มี id="roomAvailability" เพื่อแสดงผล
      }
    });
  });
  