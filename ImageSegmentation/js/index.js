var uploadImage;
var segmentationValue;

$(document).ready(function () {
    $("#seg").click(function () {
        segmentationValue = $("#list option:selected").val();
        // debugger
        $.get("http://localhost:8080/image",{
            uuid:uploadImage,
            segSign:segmentationValue
        },function () {
            $("#result").attr("src", "images/image_"+uploadImage+".png");
            alert("Success" + segmentationValue);
        });

    });
    
    $("#button_upload").click(function (event) {

    });

    $("#selectFile").change(function () {
        readURL(this);
    });

    function readURL(input) {
        if(input.files && input.files[0]){
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#seg").removeAttr("disabled");
                $("#upload").attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
        var file = new FormData();
        uploadImage = input.files[0].name;

        file.append("file", input.files[0]);
        debugger
        // upload the file
        $.ajax({
            url:"http://localhost:8080/upload/",
            type:"POST",
            data:file,
            async: false,
            cache: false,
            contentType: false,
            processData: false,
            success:function(returnData){
                if($.trim(returnedData)==$.trim("success"))
                {
                    alert("上传图片成功");
                }
                else if($.trim(returnedData)==$.trim("fail"))
                    alert("上传图片失败");
            }
        });
    }

});
