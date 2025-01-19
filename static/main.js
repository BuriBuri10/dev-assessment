Dropzone.autoDiscover = false

const myDropzone = new Dropzone('#mydropzone', 
    {
    url: "upload/",
    maxFiles:1,
    maxFilesize:1,
    acceptedFiles:'.jpg',
})