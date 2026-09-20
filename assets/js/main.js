/* Meantime - progressive enhancement only.
   Nothing here is required for the page to be readable. */

(function () {
  "use strict";

  // Mark today's row in any hours list. Rows carry data-day="0".."6" (Sunday = 0).
  function markToday() {
    var today = String(new Date().getDay());
    var rows = document.querySelectorAll("[data-day]");
    for (var i = 0; i < rows.length; i++) {
      if (rows[i].getAttribute("data-day") === today) {
        rows[i].setAttribute("data-today", "true");
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", markToday);
  } else {
    markToday();
  }
})();
