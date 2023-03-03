$("#spnFightOn").hide();
$("#spnFightEnd").hide();

function sse_pelea(event) {
    event.preventDefault();

    let archivo = $("#hdnFileName").val();

    if (archivo.trim() == "") {
        alert("Por favor seleccione un archivo del listado superior.");
        return false;
    }

    $("#spnFightIdle").hide();
    $("#spnFightOn").show();

    const evtSource = new EventSource("sse/");

    //Eventos de golpe (únicos por ahora)
    evtSource.addEventListener("comment",function (event) {
        let msg = event.data;

        if (msg.trim() != "") {
            if (msg.slice(0,1) == "-") {
                $("#divRelato").append("<p>"+msg+"</p>");
            } else {
                $("#divRelato").append("<p class='text-danger'>"+msg+"</p>");
            }
        }
    });

    //Cierre del EventSource con el último 'mensaje'
    evtSource.addEventListener("exit", function(event) {
        evtSource.close();
        $("#spnFightOn").hide();
        $("#spnFightEnd").show();
    });

    //Control de error
    evtSource.onerror = function(err) {
        evtSource.close();
        console.error("EventSource failed :", err);
        $("#spnFightOn").hide();
        $("#spnFightEnd").show();
    };
}