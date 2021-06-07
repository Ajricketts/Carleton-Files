package carleton.comp1601.intentdemo

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import androidx.appcompat.app.AppCompatActivity

class SplashScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.splashscreen)
        Log.d(appName, "Splash screen created")
    }

    fun startMain(v: View) {
        Log.d(appName, "Starting Main button pressed")
        intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
        Log.d(appName, "Starting Main intent sent")
    }
}
