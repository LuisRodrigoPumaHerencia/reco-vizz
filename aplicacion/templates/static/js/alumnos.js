busqueda = document.getElementById("cbxBusqueda");
input = document.getElementById("input");
busqueda.addEventListener("change", function() {
    if(busqueda.value==1){
        input.type = 'number';
    } else if(busqueda.value==4){
        input.type = 'number';
    }else{
        input.type ='text';
    }
    input.value="";
});

