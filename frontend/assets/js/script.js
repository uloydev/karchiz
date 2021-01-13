$(document).ready(function () {
    bsCustomFileInput.init()
  })

const urlPath = window.location.pathname
// events page
if (urlPath == '/events') {
    $('#categoryInput').change(() => {
        window.location.href = '/events?category=' + $('#categoryInput').val()
    })
}