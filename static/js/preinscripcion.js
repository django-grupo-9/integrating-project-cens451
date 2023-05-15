function CheckboxChange() {
    var checkbox = document.getElementById('id_ex_alumno');
    var changeDisplayDiv = document.getElementById('change_display');
    
    if (checkbox.checked) {
      changeDisplayDiv.style.display = 'none';
    } else {
      changeDisplayDiv.style.display = 'block';
    }
  }

document.addEventListener('DOMContentLoaded', function() {
    var paisField = document.getElementById('id_pais');
    var provinciasField = document.getElementById('id_provinciaColegio');

    paisField.addEventListener('change', function() {
      if (paisField.value === 'Argentina') {
        provinciasField.disabled = false;
        provinciasField.required = true;
      } else {
        provinciasField.disabled = true;
        provinciasField.required = false;
      }
    });

    paisField.dispatchEvent(new Event('change'));
  });

