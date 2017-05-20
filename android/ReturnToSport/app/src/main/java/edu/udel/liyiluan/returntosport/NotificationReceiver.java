package edu.udel.liyiluan.returntosport;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.media.RingtoneManager;
import android.net.Uri;
import android.support.v4.app.NotificationCompat;
import android.util.Log;


public class NotificationReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
        Intent repeating_intent = new Intent(context,LoginActivity.class);
        repeating_intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);

        Uri alarmSound = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
        PendingIntent pendingIntent = PendingIntent.getActivity(context,100,repeating_intent,PendingIntent.FLAG_UPDATE_CURRENT);
        NotificationCompat.Builder builder = new NotificationCompat.Builder(context).
                setSmallIcon(R.drawable.notification).
                setContentIntent(pendingIntent).
                setContentText("Time to fill up your survey!").
                setContentTitle("Your Survey is ready").
                setSound(alarmSound).
                setAutoCancel(true);
        notificationManager.notify(100,builder.build());

    }
}
