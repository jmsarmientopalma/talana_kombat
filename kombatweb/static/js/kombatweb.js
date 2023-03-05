$(".color-td").click( function() {
    archivo = $(this).text();

    csrf = $("[name='csrfmiddlewaretoken'").eq(0).val();

    // $("#hdnFileName").val(archivo);
    $("#spnShowFileName").html(archivo);

    data = {
        "archivo" : archivo,
        "csrfmiddlewaretoken" : csrf
    }

    $.ajax({
        type: "POST",
        url: "ajax/",
        data: data,
        dataType: "json",
        success: function (response) {
            console.log(response);
            $("#codeJson").html(JSON.stringify(response))
        }
    });
});

eliminar = (archivo) => {
    const regexp = /^\w+.(json)$/ig

    if (regexp.test(archivo)) {
        path = 'delete/' + archivo.trim().toLowerCase();
        location.assign(path); 
    } else {
       alert('El parámetro es incorrecto.'); 
    }
}