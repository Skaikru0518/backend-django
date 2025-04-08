function lekerdezes() {
  fetch("http://127.0.0.1:8000/api/bejelentesek")
    .then((response) => response.json())
    .then((result) => {
      //console.log(result);
      result.forEach((element) => {
        document.querySelector("#racs").innerHTML += `
        <div class='col-12 col-md-6 col-lg-3'>
          <div class="card">
            <div class="card-header"> 
            <h2>Város: ${element.varos.varosNev}</h2>
            </div>
            <div class="card-body">
            <div>
               Utca: ${element.utca} utca <br/>
               Dátum: ${element.datum} <br/>
               Bejelento: ${element.bejelento} <br/>
            </div>
            <div class="card-footer">
              Hibás lámpák száma: ${element.lampatestek}
            </div>
          </div>
        </div>
        `;
      });
    });
}
lekerdezes();
