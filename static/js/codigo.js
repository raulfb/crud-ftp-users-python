$(document).ready(function () {


    // borrado de usuarios
    $(".buser").on('click',function () {
       
        event.preventDefault(); 

        var row = $(this).closest("tr");
        var userid = row.find("#userid").text();
        var usuarionombre = row.find("#nombre").text();

        var opcion = confirm("Estas apunto de borrar los backup's del usuario. Por favor, confirma que deseas eliminarlos");
            if (opcion == true) {
                $.ajax({
                    url: '/borrar/' + userid + '/',
                    type: 'post',
        
                    success: function (response) {
                        $("#usuario_eliminado").removeClass("clase_oculta").addClass("alert alert-success centrado")
                        $( "#usuario_eliminado" ).fadeOut( 2000, function() {
                            $("#usuario_eliminado").removeClass("alert alert-success centrado").addClass("clase_oculta")
                            location.reload();
                          });
                        row.css("display", "none");
                          
                    },
                    error: function(response) {
                        $("#error_eliminar_usuario").removeClass("clase_oculta").addClass("alert alert-danger centrado")
                        location.reload();
                    }
                });
                
            }  
    });

    

    // Popup insercción usuario
    $("a[rel='pop-up']").on('click',function () {

        var caracteristicas = "height=700,width=800,scrollTo,resizable=1,scrollbars=1,location=0";
        nueva = window.open(this.href, 'Popup', caracteristicas);
        return false;
    
    });

    // popup modificacion contraseña 
    $(".open").on("click", function () {
        $("#modalmodificacion").modal("show")
        var row = $(this).closest("tr");
        var userid = row.find("#userid").text();
        $("#idusuario").val(userid)
    });


    // comprobacion de si se modifica el campo clave formularion insercción 
    $(document).on('change', '#clave', function () {

        if ($("#clave").val() === $("#confirm").val() && $("#clave").val() != null && $("#clave").val() != null) {
            $("#fin").removeClass("clase_oculta").addClass("btn btn-success")
        } else {   
            $("#fin").removeClass("btn btn-success").addClass("clase_oculta")   
        }

    });


    // comprobacion de si se modifica el campo confirmar formulario insercción
    $(document).on('change', '#confirm', function () {
        
        if ($("#clave").val() === $("#confirm").val() && $("#clave").val() != null && $("#clave").val() != null) {
            $("#fin").removeClass("clase_oculta").addClass("btn btn-success")   
        } else {   
            $("#fin").removeClass("btn btn-success").addClass("clase_oculta")
        }
    
    });


    // comprobacion de si se modifica el campo clave formulario de modificacion de claves 
    $(document).on('change', '#clave2', function () {
        
        if ($("#clave2").val() === $("#confirm2").val() && $("#clave2").val() != null && $("#clave2").val() != null) {
            $("#fin2").removeClass("clase_oculta").addClass("btn btn-success")
        } else { 
            $("#fin2").removeClass("btn btn-success").addClass("clase_oculta") 
        }
    
    });   

    // comprobacion de si se modifica el campo Confirm formulario de modificacion de claves 
    $(document).on('change', '#confirm2', function () {
        
        if ($("#clave2").val() === $("#confirm2").val() && $("#clave2").val() != null && $("#clave2").val() != null) {
            $("#fin2").removeClass("clase_oculta").addClass("btn btn-success")
        } else {
            $("#fin2").removeClass("btn btn-success").addClass("clase_oculta") 
        }
    
    });


    // Comprobación de si se modifica el usuario
    $(document).on('change', '#usuario', function () {
        
        $("#errorborrado").addClass("clase_oculta")
    
    });


    // Modificar la contraseña del usuario
    $("#modform").submit(function (event) {

        event.preventDefault();

        var contra = $("#clave2").val();
        var idusuario=$("#idusuario").val()

        $.ajax({

            url: '/modificar/' + contra + '/'+ idusuario + '/',
            type: 'post',

            success: function (response) {
                $("#usuario_editado").removeClass("clase_oculta").addClass("alert alert-success centrado")
                $("#usuario_editado").fadeOut( 800, function() {
                   
                  });
            
                  function reload() {
                    document.location.reload();
                  }
                  setTimeout(reload, 801);

            },error: function(response) {
                alert("Se ha produccido un error al intentar modificar la clave del usuario")
            }    
        });
        
    });

 
    // Formulario de insertado de usuarios
    $("#insertform").submit(function (event) {

        event.preventDefault(); 

        var a = $("#usuario").val()
        var b = $("#confirm").val()

          $.ajax({

            url: '/insertar/' + a + '/'+ b + '/',
            type: 'post',

            success: function (response) {
                
                $("#usuario_insertado").removeClass("clase_oculta").addClass("alert alert-success centrado")
                $("#usuario_insertado").fadeOut( 800, function() {
                   
                  });
            
                  function reload() {
                    document.location.reload();
                  }
                  setTimeout(reload, 801);

            },
            error: function(response) {
                
                $("#errorborrado").removeClass("clase_oculta")   
            }  
            
        });
    
    });
   

});
