package carleton.comp1601.intentdemo

import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import android.content.Intent
import android.net.Uri
import android.view.MotionEvent

val appName = "IntentDemo"

class MainActivity : AppCompatActivity() {
    private lateinit var circle: View

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        circle = findViewById(R.id.circle)
        circle.setOnTouchListener(trackCircle)

        Log.d(appName, "Main screen created")
    }

    fun openPage(v: View) {
        Log.d(appName, "Opening URL")
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://homeostasis.scs.carleton.ca/wiki"))
        startActivity(intent)
        Log.d(appName, "URL intent sent")
    }

    val trackCircle = object: View.OnTouchListener {
        override fun onTouch(v: View?, event: MotionEvent?): Boolean {
            if (event == null || v == null) {
                return false
            }

            val action = event.getAction()
            val x = event.rawX - 128F
            val y = event.rawY - 128F

            if (action == MotionEvent.ACTION_DOWN) {
                Log.d(appName, "Circle touched at ${x}, ${y}")
            } else if (action == MotionEvent.ACTION_UP) {
                circle.x = x
                circle.y = y
                Log.d(appName, "Circle released at ${x}, ${y}")
            } else if (action == MotionEvent.ACTION_MOVE) {
                circle.x = x
                circle.y = y
                Log.d(appName, "Circle repositioned to ${x}, ${y}")
            }
            return true;
        }
    }
}
