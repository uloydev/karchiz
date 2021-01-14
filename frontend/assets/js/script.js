$(document).ready(function () {
    bsCustomFileInput.init()
  })

const urlPath = window.location.pathname
// events page
if (urlPath == '/events') {
    const orderForm = $('#orderForm')
    const inpputTicketId = $('input[name="ticket_id"]')
    $('#categoryInput').change(() => {
        window.location.href = '/events?category=' + $('#categoryInput').val()
    })
    $('.btn-order').click(function (e) {
        e.preventDefault()
        inpputTicketId.val($(this).data('ticket-id'))
        orderForm.submit()
    })
}