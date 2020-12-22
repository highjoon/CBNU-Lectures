const sequelize = require('sequelize');

module.exports = class Auction extends sequelize.Model {
  static init(sequelize) {
    return super.init({
      bid: {
        type: sequelize.INTEGER,
        allowNull: false,
        defaultValue: 0,
      },
      msg: {
        type: sequelize.STRING(100),
        allowNull: true,
      },
    }, {
      sequelize,
      timestamps: true,
      paranoid: true,
      modelName: 'Auction',
      tableName: 'auctions',
      charset: 'utf8',
      collate: 'utf8_general_ci',
    });
  }

  static associate(db) {
    db.Auction.belongsTo(db.User);
    db.Auction.belongsTo(db.Good);
  }
};
