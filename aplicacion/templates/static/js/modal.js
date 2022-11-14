$(document).ready(function () {
    $("tr #deleteUser").click(function (e) {
        e.preventDefault();
        var cod = $(this).parent().find('#codigo').val();
        var nombres = $(this).parent().find('#nombres').val();
        var apellidos = $(this).parent().find('#apellidos').val();
        swal({
            title: "¿Estás seguro de eliminar a " + nombres + " " + apellidos + "?",
            text: "¡Una vez eliminado deberá agregar de nuevo!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Sí, Eliminar!",
            cancelButtonClass: "btn-primary",
            cancelButtonText: "No, Cancelar!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (isConfirm) {
            if (isConfirm) {
                eliminarUsuario(cod);
                swal("Eliminado!", "El alumno se ha eliminado", "success");
                setTimeout(function () {
                    parent.location.href = "ServletAlumno?metodo=listar"
                }, 1800);
            } else {
                swal("Cancelado", "Cancelaste la eliminación", "error");
            }
        });
    });

    function eliminarUsuario(cod) {
        var url = "ServletAlumno?metodo=eliminar&id=" + cod;
        console.log("eliminado");
        $.ajax({
            type: 'POST',
            url: url,
            async: true,
            success: function (r) {

            }
        });
    }
});
$(document).ready(function () {
    $("tr #deleteCurso").click(function (e) {
        e.preventDefault();
        var codCurso = $(this).parent().find('#codigo').val();
        var nombreCurso = $(this).parent().find('#NombreCurso').val();
        swal({
            title: "¿Estás seguro de eliminar el curso de " + nombreCurso + "?",
            text: "¡Una vez eliminado deberá agregar de nuevo!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Sí, Eliminar!",
            cancelButtonClass: "btn-primary",
            cancelButtonText: "No, Cancelar!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (isConfirm) {
            if (isConfirm) {
                eliminarUsuario(codCurso);
                swal("Eliminado!", "El curso se ha eliminado", "success");
                setTimeout(function () {
                    parent.location.href = "ServletCurso?metodo=listar"
                }, 1800);
            } else {
                swal("Cancelado", "Cancelaste la eliminación", "error");
            }
        });
    });

    function eliminarUsuario(codCurso) {
        var url = "ServletCurso?metodo=eliminar&id=" + codCurso;
        console.log("eliminado");
        $.ajax({
            type: 'POST',
            url: url,
            async: true,
            success: function (r) {

            }
        });
    }
});
$(document).ready(function () {
    $("tr #deleteNota").click(function (e) {
        e.preventDefault();
        var codNota = $(this).parent().find('#codigo').val();
        swal({
            title: "¿Estás seguro de eliminar este registro?",
            text: "¡Una vez eliminado deberá agregar de nuevo!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Sí, Eliminar!",
            cancelButtonClass: "btn-primary",
            cancelButtonText: "No, Cancelar!",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (isConfirm) {
            if (isConfirm) {
                eliminarUsuario(codNota);
                swal("Eliminado!", "El registro se ha eliminado", "success");
                setTimeout(function () {
                    parent.location.href = "ServletNotas?metodo=listar"
                }, 1800);
            } else {
                swal("Cancelado", "Cancelaste la eliminación", "error");
            }
        });
    });

    function eliminarUsuario(codNota) {
        var url = "ServletNotas?metodo=eliminar&id=" + codNota;
        console.log("eliminado");
        $.ajax({
            type: 'POST',
            url: url,
            async: true,
            success: function (r) {

            }
        });
    }
});
