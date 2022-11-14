var busqueda = document.getElementById("cbxBusqueda");
var input = document.getElementById("input");
busqueda.addEventListener("change", function() {
    if(busqueda.value==1){
        input.type = 'number';
    }else{
        input.type ='text';
    }
    input.value="";
});

