package carleton.comp1601.picviewer2a

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

val appName = "PicViewer2A"
val pics = arrayOf(R.drawable.kittens, R.drawable.roshi, R.drawable.fish)
val picNames = arrayOf("Kittens", "Roshi", "Fish")

class MainActivity : AppCompatActivity() {
    private lateinit var p: ImageView
    private var pic = R.drawable.kittens
    private var picIndex = 0
    private lateinit var rotationInput: EditText
    private lateinit var scaleInput: EditText
    private lateinit var pXInput: EditText
    private lateinit var pYInput: EditText
    private lateinit var image_title: TextView
    var xCoordinate: Float = 0F
    var yCoordinate: Float = 0F

    val r = PicWatcher("rotation", 0F, ::updateImage)
    {r ->
        if (r > 720F) return@PicWatcher 720F
        if (r < 0F) return@PicWatcher 0F
        r
    }
    val s = PicWatcher("scale", 1F, ::updateImage)
    {s ->
        if (s > 5F) return@PicWatcher 5F
        if (s < 0) return@PicWatcher 0F
        s
    }
    val X = PicWatcher("X", 0F, ::updateImage, ::clamp_xy)
    val Y = PicWatcher("Y", 0F, ::updateImage, ::clamp_xy)

    fun clamp_xy(v: Float): Float {
        if (v > 1000F) return 1000F
        if (v < -1000F) return -1000F
        return v
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        if (savedInstanceState != null) {
            // do something
        }

        p = findViewById(R.id.mypic)
        p.setOnTouchListener(trackImage)

        image_title = findViewById(R.id.imageTitle)

        rotationInput = findViewById(R.id.rotation)
        rotationInput.addTextChangedListener(r)

        scaleInput = findViewById(R.id.scale)
        scaleInput.addTextChangedListener(s)

        pXInput = findViewById(R.id.x)
        pXInput.addTextChangedListener(X)

        pYInput = findViewById(R.id.y)
        pYInput.addTextChangedListener(Y)

        updateImage()
        Log.d(appName, "Activity Created")
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.run {
            putString("X", X.value.toString())
            putString("Y", Y.value.toString())
            putString("rotation", r.value.toString())
            putString("scale", s.value.toString())
        }
        super.onSaveInstanceState(outState)
        Log.d(appName, "State saved")
    }

    fun updateImage() {
        p.setImageResource(pic)
//        p.tag = pics[picIndex].toString().substring(0, pics[picIndex].toString().lastIndexOf('.'))
        image_title.text = picNames[picIndex]
        Log.d(appName, "Title Name updated to ${image_title.text}")
        p.x = X.value
        p.y = Y.value
        p.rotation = r.value
        p.scaleX = s.value
        p.scaleY = s.value
    }

    fun nextImage(v: View) {
        picIndex = (picIndex + 1) % pics.size
        pic = pics[picIndex]
        updateImage()
    }

    fun openPage(v: View) {
        Log.d(appName, "Opening URL")
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://duckduckgo.com/?q=" + picNames[picIndex] + "&iax=images&ia=images"))
        startActivity(intent)
        Log.d(appName, "URL intent sent")
    }

    val trackImage = object: View.OnTouchListener {
        override fun onTouch(v: View?, event: MotionEvent?): Boolean {
            if (event == null || v == null) {
                return false
            }

            val action = event.action

            if (action == MotionEvent.ACTION_DOWN) {
                xCoordinate = v.getX() - event.getRawX()
                yCoordinate = v.getY() - event.getRawY()
                Log.d(appName, "Image repositioned to ${xCoordinate}, ${yCoordinate}")
            } else if (action == MotionEvent.ACTION_UP) {
                Log.d(appName, "Image repositioned to ${xCoordinate}, ${yCoordinate}")
            } else if (action == MotionEvent.ACTION_MOVE) {
                v.animate().x(event.getRawX() + xCoordinate).y(event.getRawY() + yCoordinate).setDuration(0).start();
                pXInput.setText((event.getRawX() + xCoordinate).toString())
                pYInput.setText((event.getRawY() + yCoordinate).toString())
                Log.d(appName, "Image repositioned to ${xCoordinate}, ${yCoordinate}")
            }
            return true;
        }
    }
}

class PicWatcher(n: String, v: Float, u: () -> Unit, c: (Float) -> Float) : TextWatcher {
    var value: Float = v
    var default_value: Float = v
    var name: String = n
    var update: () -> Unit = u
    var clamp: (Float) -> Float = c

    override fun afterTextChanged(s: Editable) {
        val new_value = s.toString().toFloatOrNull()

        if (new_value != null) {
            value = clamp(new_value)
            Log.d(appName, "Set ${name} to ${value}.")
        } else {
            value = default_value
            Log.d(appName, "Set ${name} to default value ${value}.")
        }

        update()
    }

    override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
    }

    override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
    }

}


//                if (xCoOrdinate ==v.getX() - event.getRawX() && yCoOrdinate == v.getY() - event.getRawY())
//                    v.performClick()