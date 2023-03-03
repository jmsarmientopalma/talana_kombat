$(".color-td").click( function() {
    archivo = $(this).text();

    csrf = $("[name='csrfmiddlewaretoken'").eq(0).val();

    $("#hdnFileName").val(archivo);

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