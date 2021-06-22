// function Task_1(a, b) {
//     return a + b
// }
// console.log(Task_1(2, 3))
//
// function Task_2(a, b) {
//     d = {}
//     d.a = a
//     d.b = b
//     return d
// }
// console.log(Task_2(2, 3))
//
// function Task_3(a) {
//     if (a.indexOf(8) != -1 || a.indexOf(4) != -1) {
//         return true
//     } else {
//         return false
//     }
// }
// console.log(Task_3([3, 5, 6, 8]))
//
// function fn4(a, b) {
//     x = a[1] / b[0]
//     return x
// }
// console.log(fn4([4, 6, 8], [2, 3, 4]))

$( document ).ready(function () {
    // $('#btn_reg').click(function (e) {
    //     x = $('#login').val()
    //     if (x.length < 3) {
    //         alert('В логине должно быть больше 3 символов')
    //         e.preventDefault()
    //     }
    // })
    // $('#btn_reg').click(function (e) {
    //     x = $('#password').val()
    //     if (x.length < 3) {
    //         alert('В пароле должно быть больше 3 символов')
    //         e.preventDefault()
    //     }
    // })
    $('#login').blur(function () {
        $.post(
            'username_check',
            {
                'check': $('#login').val()
            },
            function (response) {
                if (response.username == 'y') {
                    alert('Такой юзер есть')
                }
            }
        )
    })
    $('#btn_reg').click(function (e) {
        $.post(
            'reg',
            {
                'username': $('#login').val(),
                'email': $('#email').val(),
                'password': $('#password').val()
            },
            function (response) {
            if (response.status == 'ok') {
                alert('Well done')
                window.location.pathname = '/'
            }
            }
        )
    })
})

