const coti = document.querySelector(".cotizacion");

fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(res => res.json())
    .then(data => {
        for (const ele of data) {
            imprimir(ele.casa.nombre, ele.casa.compra, ele.casa.venta, ele.casa.variacion);
        }
    });

function imprimir(nombre, compra, venta, variacion){
  if (nombre !== 'Argentina' && nombre !== 'Dolar Soja' && nombre !== 'Dolar') {
    // console.log(ele.casa.nombre);
    if(variacion.includes("-")){
        coti.innerHTML += 
            `<tr class = "table-danger">
            <td>${nombre}</td>
            <td>${verificacion(compra)}</td>
            <td>${verificacion(venta)}</td>
            <td>${VerVariacion(variacion)}</td>
            <td>${fecha_Actu()}</td>
            </tr>`;
    }
    else{
            coti.innerHTML += 
            `<tr class = "table-success">
            <td>${nombre}</td>
            <td>${verificacion(compra)}</td>
            <td>${verificacion(venta)}</td>
            <td>${VerVariacion(variacion)}</td>
            <td>${fecha_Actu()}</td>
            </tr>`;
        }
}
}

function VerVariacion(varia) {
  if (varia == undefined) {
    return "-";
  } else {
    return varia + "%";
  }
}
function fecha_Actu() {
  const date = new Date();
  const dia = date.getDate();
  const mes = date.getMonth();
  const año = date.getFullYear();

  return dia + "/" + mes + "/" + año;
}
function verificacion(precio) {
  if (precio === "No Cotiza") {
    return precio;
  } else {
    return "$" + precio;

  }
}
