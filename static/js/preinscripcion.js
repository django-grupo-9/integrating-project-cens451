function CheckboxChange() {
    var checkbox = document.getElementById('id_ex_alumno');
    var changeDisplayDiv = document.getElementById('change_display');
    var estudios = document.getElementById('id_estudios');
    var colegio = document.getElementById('id_colegio');
    var pais = document.getElementById('id_pais');
    var provincia = document.getElementById('id_provinciaColegio');
    var localidad = document.getElementById('id_localidad');
    
    if (checkbox.checked) {
      changeDisplayDiv.style.display = 'none';
      estudios.required = false;
      colegio.required = false;
      pais.required = false;
      provincia.required = false;
      localidad.required = false;
    } else {
      changeDisplayDiv.style.display = 'block';
      estudios.required = true;
      colegio.required = true;
      pais.required = true;
      provincia.required = true;
      localidad.required = true;
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

