# Install packages
install.packages("twitteR")

#install.packages("rtweet")
library(rtweet)

rt_rechazo <- search_tweets(
  "#rechazo", n = 18000, include_rts = FALSE
)

rt_apruebo <- search_tweets(
  "#apruebo", n = 18000, include_rts = FALSE
)

## plot time series of tweets
rt %>%
  ts_plot("3 hours") +
  ggplot2::theme_minimal() +
  ggplot2::theme(plot.title = ggplot2::element_text(face = "bold")) +
  ggplot2::labs(
    x = NULL, y = NULL,
    title = "Frequencia de #rechazo en estados de Twitter",
    subtitle = "Twitter status (tweet) counts aggregated using three-hour intervals",
    caption = "\nSource: Data collected from Twitter's REST API via rtweet"
  )

# Representación Grafíca
library(ggplot2)

ggplot()+
  geom_point(aes(x=testing$GRE.Score,
                 y=testing$Chance.of.Admit),
             colour = "red")+
  geom_line(aes(x=testing$GRE.Score,
                y=ypred, colour = "blue"),
            alpha = 1,
            size= 0.8)+
  geom_line(aes(x=testing$GRE.Score,
                y=predict(regression, newdata = testing),
                colour = "green"), alpha = 1,
            size= 0.8)+
  scale_color_discrete(name = "Modelo", labels = c("Descenso por gradiente", 
                                                   "Regresión Lineal (lm)"))+
  ggtitle("Probabilidad admisión vs GRE Score (Conjunto de Test)")+
  xlab("GRE Score")+
  ylab("Probabilidad admisión a Postgrado")