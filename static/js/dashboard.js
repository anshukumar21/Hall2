function update() {
    let e = document.querySelector("canvas").chart;
    var t = e.data.datasets[0].label;
    if (console.log(t), "monthly" == t) {
        var a = [18, 30, 0, 50, 35, 10, 20];
        let e = document.querySelector("canvas").chart;
        e.data.datasets[0].label = "weekly", e.data.labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], e.data.datasets[0].data = a, e.update()
    } else {
        a = [300, 240, 250, 314, 298];
        e.data.labels = ["Nov", "Dec", "Jan", "Feb", "Mar"], e.data.datasets[0].label = "monthly", e.data.datasets[0].data = a, e.update()
    }
}

function give_title() { return "monthly" == document.querySelector("canvas").chart.data.datasets[0].label ? "Show data of this week" : "Show data of this month" }
document.addEventListener("DOMContentLoaded", (function() {
    [].slice.call(document.querySelectorAll("[data-bss-tooltip]")).map((function(e) { return new bootstrap.Tooltip(e) }));
    var e = document.querySelectorAll("[data-bss-chart]");
    for (var t of e) t.chart = new Chart(t, JSON.parse(t.dataset.bssChart))
}), !1), $(document).ready((function() { $("[data-bs-toggle=tooltip]").mouseenter((function() { $(this).attr("title", give_title()) })) }));
const qrcode = window.qrcode,
    video = document.createElement("video"),
    canvasElement = document.getElementById("qr-canvas"),
    canvas = canvasElement.getContext("2d"),
    qrResult = document.getElementById("qr-result"),
    outputData = document.getElementById("outputData"),
    btnScanQR = document.getElementById("btn-scan-qr");
let scanning = !1;

function tick() { canvasElement.height = video.videoHeight, canvasElement.width = video.videoWidth, canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height), scanning && requestAnimationFrame(tick) }

function scan() { try { qrcode.decode() } catch (e) { setTimeout(scan, 300) } }
qrcode.callback = e => { e && (outputData.innerText = e, scanning = !1, video.srcObject.getTracks().forEach((e => { e.stop() })), qrResult.hidden = !1, canvasElement.hidden = !0, btnScanQR.hidden = !1) }, btnScanQR.onclick = () => { navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } }).then((function(e) { scanning = !0, qrResult.hidden = !0, btnScanQR.hidden = !0, canvasElement.hidden = !1, video.setAttribute("playsinline", !0), video.srcObject = e, video.play(), tick(), scan() })) };