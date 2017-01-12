# Optimization of weights

# optimization function
fn = function(w) {
    # results of 1st round should match:
    50000 * sum( (apply(X * w,1,sum) - results1)^2 ) +
    # results of the 2nd round should match:
    50000 * sum( (apply(X * w,2,sum) - results2)^2 ) +
    # loss function 1, the weights should not be far from 1:
    sum( c(t(w-1) %*% (w-1)) ) +
    # loss function 2, the rate shall be similar to zeman / schwarzenberg in 1st round
    # w[,1] - w[,2] did not work in optim, so workaround:
    #1.669086312/0.719913577 is rate of respondents for zeman / schwarzenberg in 1st round
    sum( (apply(w*onezero,1,sum) / apply(w*zeroone,1,sum) - 1.669086312/0.719913577)^2 )
}

# number of respondents
respondents = t(matrix(c(1661,0,553,653,141,369,201,527,0,3726,578,440,182,549,163,73,601,1062),nrow=2))
rownames(respondents) = c('zeman','fischer','sobotka','fischerova','schwarzenberg','dienstbier','roithova','bobosikova','franz')
colnames(respondents) = c('zeman2','schwarzenberg2')

#official election results
results1 = c(0.2421,0.1635,0.0246,0.0323,0.234,0.1612,0.0495,0.0239,0.0684)
results2 = c(0.5480,0.4519)

X = respondents/sum(c(respondents))

# help matrices:
onezero = matrix(c(1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0),nrow=9)
zeroone = matrix(c(0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1),nrow=9)

# starting values:
S = matrix(1,9,2)
S[1,2] = 0.1
S[5,1] = 0.1

# optimization:
parameters = optim(S,fn,control=list(maxit=20000))

out = parameters$par

rownames(out) = rownames(respondents)
colnames(out) = colnames(respondents)

# correct zeman and schwarzenberg:
out [1,2] = 0
out [5,1] = 0

# write it to file:
setwd("/home/michal/dev/president2013")
write.table(out,file="weights.csv",sep="\t")


