$('#enviarAjax').on('click', function(){
    var id_titulo_obtenido =  $('#id_titulo_obtenido').val();
    var id_institucion =  $('#id_institucion').val();
    var id_anioGraduacion =  $('#id_anioGraduacion').val();
    var id_nivel_educacion_formal =  $('#id_nivel_educacion_formal').val();

    if(id_titulo_obtenido != "" & id_institucion != "" & id_anioGraduacion != "" &id_nivel_educacion_formal != "" )
    {

        var ed = {
            id_titulo_obtenido : id_titulo_obtenido,
            id_institucion: id_institucion,
            id_anioGraduacion: id_anioGraduacion,
            id_nivel_educacion_formal: id_nivel_educacion_formal
        };

        $.ajax({
            url: "{% url 'guardar_titulo' %}",
            type: "POST",
            data: ed,
            cache:false,
            dataType: "json",
            success: function(resp){
                var meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
                var fechaSplit = id_anioGraduacion.split("-");
                var html = `
                        <tr id="ocultar${resp.id}">
                            <td>
                            ${resp.id_titulo_obtenido}
                            </td>
                            <td>
                            ${resp.id_institucion}
                            </td>
                            <td>
                            ${fechaSplit[2]} de ${meses[fechaSplit[1]-1]} de ${fechaSplit[0]}
                            </td>
                            <td>
                            ${resp.id_nivel_educacion_formal}
                            </td>
                            <td>  
                            <button type="button" rel="tooltip" class="btn btn-danger btn-round btn-sm" onclick="eliminarTitulo(${resp.id})" >
                                            <i class="material-icons">close</i>
                            </button>
                            </td>

                        </tr>
                    `;
                   
                        $('#id_titulo_obtenido').val('');
                        $('#id_institucion').val('');
                        $('#id_anioGraduacion').val('');
                        $('#id_nivel_educacion_formal').val('');
                        let auxIns = document.querySelector('.modalInstitucion');
                        let instance = M.Modal.getInstance(auxIns);
                        instance.close();
                        
                    
            document.querySelector('.aux').innerHTML += html;
            //var a = json_loads(resp)

            //console.log(a);
                }
            });
            //Fin de la peticion AJAX

        }
        else{
            alert("Por favor llena todos los campos");
        }
    });

$('#enviarAjaxParticipaciones').on('click',function(){
    

    var id_tipoDeComunidad =  $('#id_tipoDeComunidad').val();
    var id_nombreDeLaComunidad =  $('#id_nombreDeLaComunidad').val();
    var id_ambito =  $('#id_ambitoParticipacion').val();
    
    if(id_tipoDeComunidad != "" && id_nombreDeLaComunidad != "" && id_ambito != ""){


    var ed = {
        id_tipoDeComunidad : id_tipoDeComunidad,
        id_nombreDeLaComunidad: id_nombreDeLaComunidad,
        id_ambito: id_ambito
    };

    $.ajax({
            url: "{% url 'guardar_participacion' %}",
            type: "POST",
            data: ed,
            cache:false,
            dataType: "json",
            success: function(resp){
                
                var html = `
                        <tr id="ocultarComunidad${resp.id}">
                            <div>
                                <td>
                                    ${resp.id_tipoDeComunidad}
                                </td>
                                <td>
                                    ${resp.id_nombreDeLaComunidad}
                                </td>

                                <td>
                                    ${resp.id_ambito}
                                </td>
                                <td>
                                    <button type="button" rel="tooltip" class="btn btn-danger btn-round btn-sm" onclick="eliminarTituloParticipaciones(${resp.id})" >
                                            <i class="material-icons">close</i>
                                    </button>
                                </td>
                            </div>
                        </tr>
                    `;

            document.querySelector('.auxParticipaciones').innerHTML += html;
                $('#id_tipoDeComunidad').val('');
                $('#id_nombreDeLaComunidad').val('');
                $('#id_ambitoParticipacion').val('');
                let aux = document.querySelector('.modalParticipaciones');
                var instance = M.Modal.getInstance(aux);
                instance.close();

                }
            });


    }
    else{
        alert("Por favor complete todos los campos")
    }

        });

$('#agregarReconocimientoAjax').on('click', function(){
    var id_titulo_obtenido_reconocimiento =  $('#id_titulo_obtenido_reconocimiento').val();
    var id_institucionReconocimiento =  $('#id_institucionReconocimiento').val();
    var id_anioReconocimiento =  $('#id_anioReconocimiento').val();
    var id_ambito =  $('#id_ambito').val();

    if(id_titulo_obtenido_reconocimiento != "" && id_institucionReconocimiento != "" && id_anioReconocimiento != "" && id_ambito != ""){

    var ed = {
        id_titulo_obtenido_reconocimiento : id_titulo_obtenido_reconocimiento,
        id_institucionReconocimiento: id_institucionReconocimiento,
        id_anioReconocimiento: id_anioReconocimiento,
        id_ambito: id_ambito
    };

    $.ajax({
        url: "{% url 'guardar_reconocimiento' %}",
        type: "POST",
        data: ed,
        cache:false,
        dataType: "json",
        success: function(resp){
            var meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
             var fechaSplit = id_anioReconocimiento.split("-");
            var html = `

                <tr id="ocultarReconocimiento${resp.id}">
                        <div>
                                <td>
                                    ${resp.id_titulo_obtenido_reconocimiento}
                                </td>
                                <td>
                                    ${resp.id_institucionReconocimiento}
                                </td>

                                <td>
                                    ${fechaSplit[2]} de ${meses[fechaSplit[1]-1]} de ${fechaSplit[0]}
                                </td>
                                <td>
                                    ${resp.id_ambito}
                                </td>

                                <td>
                                    <button type="button" rel="tooltip" class="btn btn-danger btn-round btn-sm" onclick="eliminarReconocimiento(${resp.id})" >
                                            <i class="material-icons">close</i>
                                    </button>
                                </td>
                        </div>
                    </tr>
                `;

        document.querySelector('.auxReconocimiento').innerHTML += html;
            $('#id_titulo_obtenido_reconocimiento').val('');
            $('#id_institucionReconocimiento').val('');
            $('#id_anioReconocimiento').val('');
            $('#id_ambito').val('');

            let aux = document.querySelector('.modalReconocimiento');
            var instance = M.Modal.getInstance(aux);
            instance.close();
            
            }
           
    });

        }else{
            console.log(id_titulo_obtenido_reconocimiento, id_institucionReconocimiento, id_anioReconocimiento, id_ambito);
            alert("Por favor complete todos los campos");
            
        }

    });

$('#guardarPublicacion').on('click', function(){
    var id_titulo_publicacion =  $('#id_titulo_publicacion').val();
    var id_anio =  $('#id_anio').val();
    var id_tipo_publicacion =  $('#id_tipo_publicacion').val();
    console.log('se fye');
    if(id_titulo_publicacion != "" && id_anio != "" && id_tipo_publicacion != ""){

    var ed = {
        id_titulo_publicacion : id_titulo_publicacion,
        id_anio: id_anio,
        id_tipo_publicacion: id_tipo_publicacion
    };

    $.ajax({
        url: "{% url 'guardar_publicacion' %}",
        type: "POST",
        data: ed,
        cache:false,
        dataType: "json",
        success: function(resp){
            var meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
             var fechaSplit = id_anio.split("-");
            var html = `
                        <tr id="ocultarPublicacion${resp.id}">
                            <div>
                                <td>
                                    ${resp.id_titulo_publicacion}
                                </td>
                                <td>
                                    ${fechaSplit[2]} de ${meses[fechaSplit[1]-1]} de ${fechaSplit[0]}
                                </td>

                                <td>
                                    ${resp.id_tipo_publicacion}
                                </td>
                                <td>
                                    <button type="button" rel="tooltip" class="btn btn-danger btn-round btn-sm" onclick="eliminarPublicacion(${resp.id})" >
                                            <i class="material-icons">close</i>
                                    </button>
                                </td>
                            </div>
                        </tr>
                `;

        document.querySelector('.auxPublicacion').innerHTML += html;
          $('#id_titulo_publicacion').val('');
            $('#id_anio').val('');
            $('#id_tipo_publicacion').val('');
            // $('#publicaciones').modal({dismissible: false});      
            // $('#publicaciones').modal('close');
            // $('#publicaciones').modal('toggle');
            let aux = document.querySelector('.modalPublicaciones');
            var instance = M.Modal.getInstance(aux);
            instance.close();

            }
          
    });

}
else{
    alert("Por favor complete todos los campos");
}
});